package com.example.vstore.controller;

import com.example.vstore.mode.User;
import com.example.vstore.DAO.UserServer;
import com.example.vstore.DAO.UserService;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

@Controller
public class SignUp {
    @Autowired
    UserServer userServer;
    @Autowired
    UserService userService;

    @GetMapping("/sign-up")
    public String signupFrom(ModelMap mode, @RequestParam(value = "error", required = false) String error){
        mode.addAttribute("msg",error);
        return "sign-up";

    }

    @PostMapping(value="/sign-up", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public String signUp(ModelMap mode,@RequestBody User user){
        User c = userServer.findByUser_name1(user.getUser_name());
        if (c != null) {
            return "/sign-up?error=User name da ton tai!";
        }
        if (user.getPassword() == null) {
            return "/sign-up?error=Hay nhap password!";
        } else if(user.getUser_name().equals(""))
            return "/sign-up?error=Hay nhap user name!";
        user.setRole("ROLE_USER");
        user.setWallet(10000L);
        userService.signUpUser(user);
        return "/login?error=Dang ky thanh cong, hay dang nhap!";
    }
}
