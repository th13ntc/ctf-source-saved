package com.example.vstore.mode;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="bill")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Bill implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private  Long id_bill;
    private Long id_user;
    //private Long id_product;

    @Temporal(TemporalType.DATE)
    @JsonFormat(pattern="yyyy-MM-dd")
    private Date date;

    private Long number;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="id_product")
    Products product;

    public Bill() {

    }
    public Bill(Long id_bill, Long id_user, Long id_product,Long number, Date date) {
        this.id_bill = id_bill;
        this.id_user = id_user;
        //this.id_product = id_product;
        this.date = date;
        this.number = number;
    }
    // get

    public Date getDate() {
        return this.date;
    }

    public Long getId_bill() {
        return id_bill;
    }

    //public Long getId_product() {
       // return id_product;
    //}

    public Long getId_user() {
        return id_user;
    }

    public Long getNumber() {
        return number;
    }

    public Products getProduct() {
        return product;
    }

    // set

    public void setDate(Date date) {
        this.date = date;
    }

    //public void setId_product(Long id_product) {
        //this.id_product = id_product;
    //}

    public void setId_user(Long id_user) {
        this.id_user = id_user;
    }

    public void setNumber(Long number) {
        this.number = number;
    }

    public void setProduct(Products product) {
        this.product = product;
    }
}
