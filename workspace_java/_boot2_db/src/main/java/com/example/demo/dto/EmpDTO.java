package com.example.demo.dto;

import java.sql.Date;
import java.util.List;

import lombok.Data;

@Data
public class EmpDTO {

	private int empno;
	private String ename;
	private String job;
	private int sal = Integer.MIN_VALUE;
	private Integer mgr;
	private Date hiredate;
	private Integer comm;
	private int deptno;
	
	private int size = 10;
	private int page = 1;
	private int start = 0;
	private int end;
	
	private String type;
	private String keyword;
	
	private List empnos;
}
