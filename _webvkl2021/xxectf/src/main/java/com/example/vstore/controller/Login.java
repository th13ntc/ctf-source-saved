package com.example.vstore.controller;

import com.example.vstore.mode.User;
import com.example.vstore.DAO.UserServer;
import com.example.vstore.DAO.UserService;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;


import javax.servlet.http.HttpSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Controller
public class Login {
    public static Logger logger = LoggerFactory.getLogger(Login.class);
    @Autowired
    UserServer userServer;

    @Autowired
    UserService userService;

    @GetMapping(value = "/login")
    public String loginFrom(ModelMap mode, HttpSession session) {
        if(session.getAttribute("user") != null) {
            return "home";
        }
        return "login_form";
    }




}
