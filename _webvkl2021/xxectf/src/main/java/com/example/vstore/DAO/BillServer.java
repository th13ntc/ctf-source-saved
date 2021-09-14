package com.example.vstore.DAO;

import com.example.vstore.mode.Bill;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BillServer extends JpaRepository<Bill, Long>{
    @Query("select b from Bill b where b.id_user=?1")
    List<Bill> findById_user(Long id_user);

}
