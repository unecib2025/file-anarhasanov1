#1
with open("users.txt", "r") as f:
    for line in f:
        print(line.strip())

#2
with open("passwords.txt", "r") as f:
    passwords = f.readlines()
with open("weak.txt", "w") as out:
    for p in passwords:
        if len(p.strip()) < 8:
            out.write(p)

#3
unique = set()
with open("ips.txt", "r") as f:
    for ip in f:
        unique.add(ip.strip())
with open("unique_ips.txt", "w") as out:
    for ip in unique:
        out.write(ip + "\n")

#4
count = 0
with open("log.txt", "r") as f:
    for _ in f:
        count += 1
print(count)

#5
with open("ports.txt", "r") as f:
    ports = f.readlines()
with open("blocked_ports.txt", "w") as out:
    for p in ports:
        p = p.strip()
        if p.isdigit() and int(p) < 1024:
            out.write(p + "\n")

#6
with open("auth.log", "r") as f:
    lines = f.readlines()
with open("failed.txt", "w") as out:
    for line in lines:
        if "FAILED" in line:
            out.write(line)

#7
with open("traffic.txt", "r") as f:
    values = f.readlines()
with open("alert.txt", "w") as out:
    for v in values:
        v = v.strip()
        if v.isdigit() and int(v) > 1000:
            out.write(v + "\n")

#8
with open("commands.txt", "r") as f:
    commands = f.readlines()

with open("safe.txt", "w") as out:
    for cmd in commands:
        if "rm" not in cmd:
            out.write(cmd)

#9
count = 0
with open("users.txt", "r") as f:
    for _ in f:
        count += 1
with open("report.txt", "w") as out:
    out.write("Всего пользователей: " + str(count))

#10
with open("full_log.txt", "w") as out:
    with open("log1.txt", "r") as f1:
        out.write(f1.read())
    with open("log2.txt", "r") as f2:
        out.write(f2.read())




"""Функция open() используется для открытия файла и получения объекта, через который выполняется чтение или запись данных.
Режим r открывает файл только для чтения, w создаёт/перезаписывает файл для записи, а a добавляет данные в конец существующего файла.
При открытии файла в режиме w его содержимое удаляется, и запись начинается с пустого файла.
read() считывает весь файл как одну строку, а readlines() возвращает список строк.
Конструкция with автоматически закрывает файл после завершения работы, предотвращая утечки и ошибки.
Чтобы добавить данные без удаления старых, используют режим a.
Файлы применяются в ИБ для хранения логов, анализа событий, контроля доступа, фиксации попыток взлома и формирования отчётности."""

