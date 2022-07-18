package com.example.vstore.DAO;

import com.example.vstore.mode.User;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.text.MessageFormat;
import java.util.Optional;

@Service
@AllArgsConstructor
public class UserService implements UserDetailsService {
    private final UserServer userServer = null;

    @Autowired
    BCryptPasswordEncoder bCryptPasswordEncoder;


    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {

        final Optional<User> optionalUser = userServer.findByUser_name(userName);

        if (optionalUser.isPresent()) {
            return optionalUser.get();
        }
        else {
            throw new UsernameNotFoundException(MessageFormat.format("User with user name {0} cannot be found.", userName));
        }
    }

    public void signUpUser(User user) {

        final String encryptedPassword = bCryptPasswordEncoder.encode(user.getPassword());
        user.setPassword(encryptedPassword);
        user.setEnabled(true);
        final User createdUser = userServer.save(user);

    }

    public void updateUser(User user) {
        User oldUser = userServer.findByUser_name1(user.getUser_name());
        if (!user.getPassword().equals("")) {
            user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
        }
        else
            user.setPassword(oldUser.getPassword());
        userServer.save(user);
    }
}
