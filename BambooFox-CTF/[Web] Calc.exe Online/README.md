# write up

Cùng nhìn tổng quan đề bài 1 xíu nhé!!!!

## Overview

![alt](http://~)

Thử 1 + 1 luôn nè:
![alt](http://~)

Ctr+U coi đi kiếm source xíu. Ồ cho file source nè:
![alt](http://~)
![alt](http://~)

Nào như mọi lần tui bắt đầu đi đọc code và kết luận vài dòng:

- Đây là code php
- Có 2 cái function
- Param của mình truyền vào là đi qua hàm **safe_eval**
- Trong **safe_eval**, nó đưa param của mình cho **is_safe** kiểm tra
- Trong **is_safe**, nó bắt đầu chạy code các kiểu -> tóm tắt lại rằng: Chỉ được dùng các hàm trong toàn học, và toán tử +-\*/
- Sau khi **is_safe** true sẽ cho chúng ta thực thi (eval), ngược lại sẽ xuất ra màn hình 1 chuỗi.

> Vậy giải pháp rút ra là phải inject vào 1 đoạn code sao cho hàm **is_safe** trả về true rồi tạo thành 1 command có nghĩa để thực thi được đến server server.
