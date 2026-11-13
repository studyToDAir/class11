package com.example.demo.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.dto.EmpDTO;
import com.example.demo.service.EmpService;

@Controller
public class EmpController {

	private static final Logger logger = LoggerFactory.getLogger(EmpController.class);
	
	@Autowired
	EmpService empService;
//	EmpService empService = new EmpServiceImpl()
	
//	@ResponseBody
	@RequestMapping(value="/", method=RequestMethod.GET)
	public String hello() {
		EmpDTO dto = new EmpDTO();
		System.out.println(dto);

		return "hello";
	}
	// 사원 목록 조회
	// "/list"로 접근하면
	// 조회하고 결과를 "list"로 담아서
	// result.jsp로 보낸다
	@GetMapping("/list")
	public String list(Model model) {
		System.out.println("/list 실행");
		
		List<EmpDTO> list = empService.getEmpList();
		System.out.println("/list: list: "+ list);
		
		model.addAttribute("list", list);
		return "result";
	}

	@RequestMapping("/getEmpno")
	public String getEmpno(Model model,
		@RequestParam(value="empno", required=false)
		int empno
	) {
		System.out.println("/getEmpno 실행");
		
		System.out.println("empno: "+ empno);
		EmpDTO empDTO = empService.getEmpno(empno);

		model.addAttribute("empDTO", empDTO);
		
		return "result";
	}

}





