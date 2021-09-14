package com.example.vstore.DAO;

import com.example.vstore.mode.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.Query;

import java.util.Optional;

import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface UserServer extends JpaRepository<User, Long>{
    @Query("select u from User u where u.user_name = ?1 and u.password = ?2")
    User findByUser_nameAndPassword(String userName, String password);

    @Query("update User u set u.wallet = ?1 where u.id_user = ?2")
    void updateWallet(Long wallet, Long id);

    @Query("select u from User u where u.id_user = ?1")
    User findById_user(Long id_user);

    @Query("select u from User u where u.user_name = ?1")
    Optional<User> findByUser_name(String userName);

    @Query("select u from User u where u.user_name = ?1")
    User findByUser_name1(String userName);


}