from fastapi import APIRouter
import traceback
import util
import pandas as pd
from typing import Any

router = APIRouter(tags=["엘라스틱서치"])

@router.get("/read/head")
# def read(fileName) :
def read(fileName : Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv') :
    print('fileName :', fileName)
    frame = util.load_csv(fileName)
    if frame is None :
        return {'ERROR': "파일을 불러오지 못했습니다"}

    '''
        head : 상위 몇 개의 데이터만 추출 (기본값 : 5)
        astype : 형변환, 기본값:NumPy.int64
        to_dict : dict로 변환
        orient='records' : 컬럼명:값 형태 
                           기본값=dict : 인덱스가 키가 된다
    '''
    preview = frame.head().astype(object).to_dict(orient='records')
    return preview

@router.get('/read/valid')
def valid():
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')
    df_ratings = util.load_csv('ratings.csv')

    # dropna : N/A 즉 결측치 즉 없는 것 제외
    notnull = df_movies['movieId'].dropna()

    # set 타입의 속성을 이용해서 id 중복 제거
    movie_ids = set(notnull)
    tag_ids = set(df_tags['movieId'].dropna())
    rating_ids = set(df_ratings['movieId'].dropna())

    result = {}
    result['no_id'] = {}
    result['no_id']['tags'] = len(tag_ids - movie_ids)
    result['no_id']['ratings'] = len(rating_ids - movie_ids)

    result['rating range'] = {}
    result['rating range']['min'] = float(df_ratings['rating'].min())
    result['rating range']['max'] = float(df_ratings['rating'].max())

    return result

def makeContent() :
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')

    # pandas
    # 데이터 프레임 : 2차원 배열
    # 시리즈 : 1차원 값
    result = pd.DataFrame()
    result['movieId'] = df_movies['movieId']
    # pandas 타입을 string 타입으로 변경 후 앞뒤공백 제거
    result['title'] = df_movies['title'].astype(str).str.strip()

    # 장르는 a|b|c 형식으로 되어있다
    # 그래서 list로 바꾸겠다
    def parse_genre(genres):
        result = []
        if str(genres).strip() == '' or str(genres).strip() == '(no genres listed)' :
            return result

        list_genre = str(genres).split('|')
        for genre in list_genre :
            # strip : 앞뒤공백 제거
            # lower : 소문자로
            result.append(genre.strip().lower())

        return result

    # 장르의 리스트가 쌓인다
    result['list_genre'] = df_movies['genres'].map(parse_genre)


    # copy() : 원본을 보존하고 사본을 가져온다
    tags = df_tags[ ['movieId', 'tag'] ].copy()

    # 공백제거 후 소문자로 변환
    tags['tag'] = tags['tag'].astype(str).str.strip().str.lower()

    # group by 처럼 중복 제거
    tags = tags.drop_duplicates(['movieId', 'tag'])

    # # pandas의 data frame 특성인데 컬림이 아니라 True인 것만 반복 시킨다
    # tags = tags[tags['tag'] != ''].drop_duplicates(['movieId', 'tag'])

    # print(tags.head())

    movie_tags = {}
    for info in tags.to_dict(orient="records") :
        id = info['movieId']
        tag = info['tag']

        # 딕셔너리의 key 중에서 id가 없으면
        if id not in movie_tags :
            # movie_tags[id] : key를 id로 만들고
            # 그 값을 리스트로 초기화
            movie_tags[id] = []
        movie_tags[id].append(tag)

    # 위 코드를 한줄로 줄이면
    # tags.groupby('movieId') : data frame인 tags를 movieId로 group by 해서
    # ['tag'] : group by 한 것에서 tag 항목을 꺼내고
    # agg(list) : 결과를 list로 만들어서
    '''
        to_dict() 까지 한 결과
        {
            movieId1 : [tag1, tag2],
            movieId2 : [tag11, tag12]
        }
    '''
    movie_tags = tags.groupby('movieId')['tag'].agg(list).to_dict()


    result['list_tag'] = df_movies['movieId'].map(lambda id : movie_tags.get(id, []))

    # 파이썬의 리스트는 + 제공
    # [1,2] + [3,4] == [1,2,3,4]

    # map : 한 컬럼을 대상으로 반복
    # apply : 모든 컬럼을 대상으로 반복
    # axis : 기본값 0
    #           0 : 위에서 아래로 읽기
    #           1 : 왼쪽에서 오른쪽으로
    result['content_text'] = result.apply(
        lambda info : " ".join( [ info['title'] ] + info['list_genre'] + info['list_tag']  ).strip(),
        axis=1
    )

    # # * : 언팩킹, js의 ...과 같음
    # # 배열을 하나씩 분리해 주는것
    # # *[1,2,3] => 1,2,3
    # result['content_text'] = result.apply(
    #     lambda info : " ".join( info['title'] , *info['list_genre'] , *info['list_tag']  ).strip(),
    #     axis=1
    # )


    # reset_index : pandas 내부 index를 재정리
    # drop=True 를 안하면 새로 추가되버린다 그래서 엉망인건 버려라
    return result.reset_index(drop=True)


@router.get('/make/content')
def content():
    dataFrame = makeContent()
    return dataFrame.head(10).to_dict(orient="records")


def makeChunk() :
    size_chunk = 50
    overlap:int = 15
    # chunks = []
    # 자료형을 미리 지정하기
    # Any : 아무형태나
    chunks : list[dict[str, Any]] = []

    dataFrame = makeContent()
    content = dataFrame.to_dict(orient="records")

    step = size_chunk - overlap
    for idx_content, info in enumerate(content) :
        text = info.get('content_text', '').strip()
        if not text :
            continue

        # for idx_start in range(0, len(text), step):
        for idx, idx_start in enumerate( range(0, len(text), step) ):
            chunk = text[idx_start : idx_start+size_chunk]
            if chunk :
                chunks.append({
                    'index': idx_content,
                    'movieId': int(info['movieId']),
                    'title': str(info['title']),
                    'genres': list(info['list_genre']),
                    'tags': list(info['list_tag']),
                    'content': chunk,
                    'chunk_index': idx,
                })

    return chunks

@router.get("/make/chunk")
def chunk():
    # dict 중에서 앞에 10개만
    return makeChunk()[0:10]


@router.get("/make/embedding/gemini")
def embedding():
    target = makeChunk()[0:10]
    actions = util.embedding_with_gemini(target)

    return actions
@router.get("/make/embedding/openai")
def embedding():
    target = makeChunk()[:10]
    print(len(target))
    actions = util.embedding_with_openai(target)

    return actions

@router.post('/es/bulk')
def bulk():
    target = makeChunk()[0:10]
    actions = util.embedding_with_gemini(target)

    # 1. 만약에 엘라스틱서치에 인덱스가 없다면 새로 만들기
    
    # 2. bulk로 넣기



