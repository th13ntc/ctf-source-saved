package com.example.vstore.mode;


import java.util.Date;

public class ViewsBill {
    private Long idProduct;
    private String nameProduct;
    private Long price;
    private Long number;
    private java.util.Date date;
    public ViewsBill(){}
    public ViewsBill(Long idProduct, String nameProduct, Long price, Long number, Date date) {
        this.idProduct = idProduct;
        this.nameProduct=nameProduct;
        this.price=price;
        this.number=number;
        this.date=date;
    }

    public void setIdProduct(Long idProduct) {
        this.idProduct = idProduct;
    }

    public void setNumber(Long number) {
        this.number = number;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public void setNameProduct(String nameProduct) {
        this.nameProduct = nameProduct;
    }

    public void setPrice(Long price) {
        this.price = price;
    }

    public Long getNumber() {
        return number;
    }

    public Date getDate() {
        return date;
    }

    public Long getIdProduct() {
        return idProduct;
    }

    public Long getPrice() {
        return price;
    }

    public String getNameProduct() {
        return nameProduct;
    }
}
