package com.example.vstore.DAO;

import java.util.List;

import javax.sql.DataSource;

import com.example.vstore.mode.Products;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import org.springframework.stereotype.Component;
@Repository
@Transactional
@Component
public class ProductsDAO extends JdbcDaoSupport {

    @Autowired
    public ProductsDAO(DataSource dataSource) {
        this.setDataSource(dataSource);
    }

    public List<Products> findUnsafeByName_product(String name) throws SQLException {
        String sql = "Select * from products where name_product = '" + name + "';";

        //List<Products> products = this.getJdbcTemplate().queryForList(sql, Products.class);
        Connection c = this.getConnection();
        ResultSet rs = c.createStatement().executeQuery(sql);

        List<Products> products = new ArrayList<>();
        while (rs.next()) {
            Products p = new Products(rs.getLong("id_product"), rs.getLong("price"),
                    rs.getLong("number"), rs.getString("name_product"), rs.getString("image"));
            products.add(p);
        }
        return products;
    }

}