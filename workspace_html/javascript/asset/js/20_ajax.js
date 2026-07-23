window.addEventListener('load', bind)

function bind(){

    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function(){

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
            console.log('다녀왔어')
            // xhr.responseText : 응답받은 글씨가 들어가 있는 변수
            console.log( xhr.responseText )

            // 깜짝 퀴즈
            // 두 번째 사람의 이름을 출력
            //      Ervin Howell
            // 세 번째 사람의 lat를 출력
            //      -68.6102
            const member = JSON.parse(xhr.responseText)
            console.log(member[1])
            console.log(member[1].name)
            console.log(member[1]['name'])
            console.log(member[2].address.geo.lat)
        }
    })

    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', '19_json.html')

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
            console.log('다녀왔어')
            console.log( xhr.responseText )
        }

        console.log( '['+ xhr.responseText +']')
    })

    const btn3 = document.querySelector('#btn3')
    btn3.addEventListener('click', function(){

        const now = new Date()
        const today = now.toISOString().split('T')[0].replace(/-/g, '')
        let hour = now.getHours() - 1
        if(hour < 10){
            hour = '0'+hour + '00'
        } else {
            hour = hour + '00'
        }
        const key = 'qVTaW2lslPLGXY2uHKVY3Vuc66ZQmC950RmMKYEg4Grvfz%2FeYbsd%2Fp4F0CzdQQwC26aBf2fTEHW76VU0OA04RQ%3D%3D'

        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        url += '?'
        url += 'serviceKey='+key
        url += '&numOfRows=1000'
        url += '&pageNo=1'
        url += '&dataType=JSON'
        url += '&base_date='+ today
        url += '&base_time='+ hour
        url += '&nx=63'
        url += '&ny=110'

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', url)

        // const q1 = document.querySelector('#q1')
        // q1.innerHTML = ''
        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
            // console.log( xhr.responseText )
            const data = JSON.parse( xhr.responseText )
            console.log( data )

            console.log( data.response.body.items.item[0].category )
            console.log( data.response.body.items.item[0].fcstValue )
            console.log( data.response.body.items.item[0].fcstTime )

            // category가 T1H(기온), RN1(강수량), REH(습도)
            let item = data.response.body.items.item
            // for(let i=0; i<item.length; i++){
            //     if(item[i].category == 'T1H'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'RN1'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'REH'){
            //         console.log(item[i])
            //     }
            // }
            let filtered = item.filter(function(data){
                if(data.category == 'T1H' 
                    || data.category == 'RN1' 
                    || data.category == 'REH'){
                    return true
                }
            })
            console.log(filtered)

            // 문제1
            // 예측카테고리 | 예측시간 | 값

/*
            <tr>
                <td>T1H</td>
                <td>0900</td>
                <td>28</td>
            </tr>
*/
            const q1 = document.querySelector('#q1')
            q1.innerHTML = ''
            for(let i=0; i<filtered.length; i++){
                const tr = document.createElement('tr')
                tr.innerHTML = `
                    <td>${filtered[i].category}</td>
                    <td>${filtered[i].fcstTime}</td>
                    <td>${filtered[i].fcstValue}</td>
                `
                q1.append(tr)
            }
            
            // 문제2
            // 시간 | 온도 | 습도 | 강수량
            let j = {
                '1000':{
                    'T1H': 20,
                    'REH': 80,
                    'RN1': '2.0 mm'
                }
            }

            j = {}
            for(let i=0; i<filtered.length; i++){
                // if( j[filtered[i].fcstTime] == undefined ){
                if( !j[filtered[i].fcstTime] ){
                    j[filtered[i].fcstTime] = {}
                }
                j[filtered[i].fcstTime][filtered[i].category] = filtered[i].fcstValue
            }
            console.log(j)

            const q2 = document.querySelector('#q2')
            let keys = Object.keys(j)
            for(let i=0; i<keys.length; i++){
                const tr = document.createElement('tr')
                tr.innerHTML = `
                    <td>${keys[i]}</td>
                    <td>${j[keys[i]]['T1H']}</td>
                    <td>${j[keys[i]]['REH']}</td>
                    <td>${j[keys[i]]['RN1']}</td>
                `
                q2.append(tr)
            }

        }
    })


    // btn4를 클릭하면
    // https://jsonplaceholder.typicode.com/users
    // 10명의 정보 중 id, name, zipcode, 회사이름을 html로 표시


    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function(){

        let a = undefined
        try{
            a.push(1)
        }catch( e ){
            console.log(e)
        }

        const url = 'https://jsonplaceholder.typicode.com/users'

        // // 1. ajax 객체 생성
        // const xhr = new XMLHttpRequest()
        // // 2. 보낼 준비
        // // 방식method, 주소
        // xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // // 3. 보내기
        // xhr.send()
        // // 4. 결과 활용
        // xhr.onload = function(){ 
            // console.log( xhr.responseText )
            // const member = JSON.parse(xhr.responseText)

        // fetch(주소, 옵션json)
        let option = {
            method: 'GET'
        }
        fetch(url, {
            method: 'GET'
        }).then(function (response){
            console.log(response)
            return response.json()
        }).then(function (data){
            console.log(data)
        }).catch(function (error){
            console.error( error )
        })
    })

}


let a = {
    a:1,
    b:2,
    a:3
}
console.log(a)

// key가 없으면 만들고
// key가 있으면 그 값에 + 1을 한다



