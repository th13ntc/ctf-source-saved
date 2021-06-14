All sources from sdctf-2021: https://github.com/acmucsd/sdctf-2021

write up: https://th13ntc.gitbook.io/blog/wu-web-san-diego-ctf

All source  challenges: https://github.com/acmucsd/sdctf-2021/tree/main/web
Apollo 1337 (EASY)

Sử dụng Burpsuite, trong hàng loạt GET request thì có một request làm mình chú ý đến:

Bỏ vào Repeater để dễ debug.

Ta thấy response về json format và lúc request thì có 1 param verbose . Thử gán giá trị vào param.

Vậy ta biết được thêm 2 endpoint mới /rocketLaunch , /fuel .
Truy cập vào rocketLaunch:

Thiếu request body dạng json vậy thì mình đổi method sang POST và conten-type là application/json

Và response bảo rằng ta thiếu trường rocket. Ta cứ thêm trường rocket vào và giá trị trống xem thế nào.

Response cho ta biết giá trị của trường rocket luôn nè!!! Tiếp tục thử

Cứ theo gợi ý của response ta thêm trường launchTime vào request body.

Responese cho ta format của launchTime và đọc lại đề bài thì ta biết thêm thời gian bắn tên lửa là giờ trưa nên gán giá trị "12:00" cho trường này.

Gợi ý tiếp theo là thêm trường pumpID . Nhưng ta không biết là id nào thì nhớ lại enpoint /fuel khi nãy tìm được, respone của /fuel :

Quay lại với endpoint /rocketLaunch ta thay thế lần lượt trường pumpID từ 1 đến 5 cho đến khi hợp lệ

ID hợp lệ ta tìm được là 4. Và reponse tiếp theo bắt ta phải tìm giá trị cho trường token @@
Để tìm giá trị của token mình bắt được keyword frontend authorization và nghĩ rằng token được để trong các file mà GET request được lúc đầu. Mình cứ click vào và ctrl+F token :>>
Và cuối cùng cũng tìm được ở 1file js

Thêm giá trị cho trường token và request lại lần nữa nào!!!

FLAG: sdctf{0ne_sM@lL_sT3p_f0R_h@ck3r$}

Gets request
(Bài này mình solve sau khi giải kết thúc)

Source index.js: https://github.com/th13ntc/ctf-source-saved/tree/main/SDCTF-05-2021/gets-request
 Từ source ta thấy được rằng server nhận param n và giới hạn n có 8 ký tự. Server truyền n là stdin của 1 chương trình C và sau khi chương trình C xử lý sẽ trả về kết quả in ra màn hình.

req.query.n sẽ nhận giá trị là string nhưng nếu ta truyền param n dưới dạng ?n[]=123456789 thì server sẽ hiểu n là 1 object/array. Lúc này length của n = 1 (độ dài của mảng chứ không phải độ dài chuỗi). Giá trị của mảng n sau khi vượt được kiểm tra BUFFER_SIZE sẽ được đưa đi làm giá trị đầu vào stdin cho chương trình C. Lúc này ta có thể buffer overflow chương trình để xuất flag.
Flag: sdctf{B3$T_0f-b0TH_w0rLds}

Git Good (MEDIUM)

Bài này nghe liên quan đến GIT nên nghĩ rằng chắc có endpoint /.git nhưng hong quý dzị ạ :>

Mình thử 1 lần nữa truy cập vào /.git/HEAD thì tải được 1 file:

Như vậy mặc dù không vào được .git nhưng mình có thể access được các file bên trong .git .
Lúc này mình cần kéo hết các file có trong .git mà không cần dùng wget. Đã có tool :>>>
GitTools: https://github.com/internetwache/GitTools

Giờ cd vào folder cgau và tiếp tục thực hiện các thao tác với git :>>

Restore lại file app.js thì ta để ý ngoài việc hash md5 thì trước khi lưu vào db còn qua 1 bước encrypt bằng thư viện bcrypt. 

Như vậy mặc dù ta có db rồi nhưng với 2 lớp encrypt thì không có hy vọng crack password :<

Check xem lịch sử commit thử.

Ồ, bcrypt chỉ vừa mới được thêm vào ở phiên bản mới nhất. Vậy ta back lại commit trước đó thử
$git checkout d8eb39e3e2bb984ce687768d20f58d962942841d
Lúc này xem lại file app.js thì đã mất đoạn compare bycrypt. Mở file users.db lên xem:

Ta thử crack password của aaron vì ông này là author của commit mới nhất :)) Password này là hash md5. Thử sử dụng tool online để crack
https://crackstation.net/

Dùng mail và password có được đăng nhập là có FLAG <3

FLAG: sdctf{1298754_Y0U_G07_g00D!}
