package com.example.vstore.controller;

import com.example.vstore.DAO.*;
import com.example.vstore.mode.Bill;
import com.example.vstore.mode.Products;
import com.example.vstore.mode.User;
import com.example.vstore.mode.ViewsBill;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.xml.sax.InputSource;
import org.xml.sax.XMLReader;
import org.xml.sax.helpers.XMLReaderFactory;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.util.*;

import javax.servlet.http.HttpSession;

@Controller
@RequestMapping("/product")
public class Product {
    @Autowired
    ProductsDAO productsDAO;

    @Autowired
    ProductsServer productsServer;

    @Autowired
    BillServer billServer;

    @Autowired
    UserServer userServer;


    @GetMapping("")
    public String listProducts(ModelMap mode) {
        List<Products> listProducts = productsServer.findAll();
        mode.addAttribute("listProducts", listProducts);
        return "list_products";
    }

    @GetMapping("/find")
    public String findProducts(ModelMap mode, @RequestParam(value = "name") String productName) {
        List<Products> listProducts = productsServer.findByName_product(productName);
        mode.addAttribute("listProducts", listProducts);
        return "list_products";
    }


    @GetMapping("/show")
    public String showProduct(ModelMap mode, @RequestParam(value="id") Long id) {
        Products product = productsServer.findByID(id);
        if (product == null) {
            mode.addAttribute("status", "ERROR");
            mode.addAttribute("title","NOT FOUND");
            mode.addAttribute("msg", "Không tìm thấy mặt hàng này!");
            return "status";
        }
        mode.addAttribute("product", product);
        return "show_product";
    }

    @PostMapping(value="/buy")
    public String buyProduct(ModelMap mode, HttpSession session, @RequestParam(value="id") Long id, @RequestParam(value="num") Long number) {
        Products product = productsServer.findByID(id);
        User user = (User) session.getAttribute("user");

        if (product.getNumber() >= number && user.getWallet() >= product.getPrice()*number) {
            User baseUser = user;
            Products baseProduct = product;
            try {
                //save bill
                Bill b = new Bill();
                b.setProduct(product);
                b.setId_user(user.getId_user());
                b.setNumber(number);
                java.util.Date utilDate = new java.util.Date();
                java.sql.Date sqlDate = new java.sql.Date(utilDate.getTime());
                b.setDate(sqlDate);
                billServer.save(b);
                //update user
                user.setWallet(user.getWallet() - (product.getPrice()*number));
                userServer.save(user);
                //update number products
                product.setNumber(product.getNumber()-number);
                productsServer.save(product);
                //done
                mode.addAttribute("status", "Thanks You");
                mode.addAttribute("title", "THÀNH CÔNG");
                mode.addAttribute("msg","Giao dịch thành công");
                return "status";
            } catch (Exception ex) {
                userServer.save(baseUser);
                productsServer.save(baseProduct);

                mode.addAttribute("status", "ERROR");
                mode.addAttribute("title", "Lỗi giao dịch");
                mode.addAttribute("msg",ex.getMessage());
                return "status";
            }

        }
        mode.addAttribute("status", "STATUS");
        mode.addAttribute("title", "GIAO DỊCH THẤT BẠI");
        mode.addAttribute("msg", "Sản phẩm không đủ hàng hoặc bạn không đủ tiền trong ví!");
        return "status";

    }
/*
    @PostMapping(value = "/showBill", produces = MediaType.APPLICATION_XML_VALUE)
    public String showBill(ModelMap mode, @RequestBody User user) {
        //check user
        User c = userServer.findById_user(user.getId_user());
        if (c == null) {
            mode.addAttribute("status", "NOT FOUND");
            mode.addAttribute("title", "Not found user");
            mode.addAttribute("msg", "Not found " + user.toString());
            return "status";
        }
        List<Bill> listBill = billServer.findById_user(user.getId_user());
        List<ViewsBill> viewsBillList =  new ArrayList<>();
        for (Bill i: listBill
             ) {
            Products gg = i.getProduct();
            viewsBillList.add(new ViewsBill(gg.getId_product(), gg.getName_product(), gg.getPrice(), i.getNumber(), i.getDate()));
        }
        mode.addAttribute("listBill", viewsBillList);

        return "_Bill";
    }*/

    @PostMapping(value = "/showBill")
    public String showBillVuln(ModelMap mode,@RequestBody String body) {
        try {
            XMLReader xmlReader = XMLReaderFactory.createXMLReader();
            xmlReader.parse(new InputSource(new StringReader(body)));  // parse xml

            mode.addAttribute("listBill", new ArrayList<>());
            return "_Bill";

        } catch (Exception e) {
            mode.addAttribute("status", "ERROR");
            mode.addAttribute("msg", "This is not BK**! ");
            return "status";
        }
    }


}
