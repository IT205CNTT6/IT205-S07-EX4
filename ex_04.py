ticket_count = input("Nhập số lượng phiếu: ")
is_valid = True
if ticket_count == "":
    is_valid = False
else:
    for char in ticket_count:
        if char < '0' or char > '9':
            is_valid = False
            break
if is_valid == False or ticket_count == "0":
    print("Số lượng phiếu không hợp lệ")
    ticket_count = 0
else:
    ticket_count = int(ticket_count)

valid_list = []

for i in range(ticket_count):

    print(f"\nNhập phiếu thứ {i + 1}")

    raw_data = input("Nhập dữ liệu: ")

    data_parts = raw_data.split("|")

    if len(data_parts) != 4:
        print("Phiếu không hợp lệ")
        continue

    student_id = data_parts[0].strip()
    student_name = data_parts[1].strip()
    email = data_parts[2].strip()
    course_name = data_parts[3].strip()

    if "@" not in email:
        print("Email không hợp lệ")
        continue

    if len(student_id) < 5:
        print("Mã học viên không hợp lệ")
        continue

    info = (
        f"Mã: {student_id} | "
        f"Tên: {student_name} | "
        f"Email: {email} | "
        f"Khóa học: {course_name}"
    )

    valid_list.append(info)

    print("Phiếu hợp lệ")

print("\n===== KẾT QUẢ =====")
print(f"Số phiếu hợp lệ: {len(valid_list)}")
for i in range(len(valid_list)):
    print(f"{i + 1}. {valid_list[i]}")