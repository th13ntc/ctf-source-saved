package com.example.vstore.DAO;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import java.util.List;
import com.example.vstore.mode.Products;

@Repository
public interface ProductsServer extends JpaRepository<Products, Long>{

    @Query("select p from Products p where p.name_product like ?1")
    List<Products> findByName_product(String name_product);

    @Query("select p from Products p where p.id_product = ?1")
    Products findByID(Long ID);

}
