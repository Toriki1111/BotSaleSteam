# Steam Daily Deal Bot

Bot tu dong quet deal Steam co muc giam gia tu 90% tro len va gui thong bao vao Discord moi ngay. Du an dung Python, CheapShark API, va GitHub Actions de chay theo lich.

## Tinh nang

- Quet deal Steam moi ngay theo lich GitHub Actions.
- Loc cac game co `savings >= 90`.
- Sap xep deal theo muc giam gia tu cao xuong thap.
- Tu dong chia danh sach thanh nhieu tin nhan Discord, toi da 10 deal moi phan.
- Ho tro chay local bang `.env` hoac chay tren GitHub bang Secrets.

## Cau truc du an

```text
.
|-- .github/
|   `-- workflows/
|       `-- daily_check.yml
|-- src/
|   |-- main.py
|   |-- notifier.py
|   `-- steam_api.py
|-- .gitignore
|-- requirements.txt
`-- README.md
```

## Yeu cau

- Python 3.11
- Discord webhook URL

## Cai dat local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Tao file `.env` tai thu muc goc:

```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_here
```

Chay thu:

```bash
python src/main.py
```

## Cai dat tren GitHub Actions

Tao repository secret ten `DISCORD_WEBHOOK_URL`:

1. Vao `Settings` -> `Secrets and variables` -> `Actions`.
2. Chon `New repository secret`.
3. Dat ten `DISCORD_WEBHOOK_URL`.
4. Dan Discord webhook URL vao gia tri secret.

Workflow duoc dinh nghia trong [.github/workflows/daily_check.yml](.github/workflows/daily_check.yml) va hien dang chay theo cron:

```yaml
0 1 * * *
```

Moc nay tuong ung 08:00 sang gio Viet Nam trong dieu kien UTC+7.

## Dau ra Discord

Moi lan chay, bot se:

- Goi CheapShark de lay deal Steam.
- Loc deal co muc giam tu 90% tro len.
- Sap xep deal theo `% savings` giam dan.
- Gui tung nhom toi da 10 embed vao Discord.

Moi embed hien thi:

- Ten game
- Link Steam Store
- Gia goc
- Gia khuyen mai
- Phan tram giam gia
- Anh header cua game

## Truong hop khong co deal

Neu khong co deal dat nguong 90%, bot chi ghi log va khong gui thong bao Discord.

## Bien moi truong

- `DISCORD_WEBHOOK_URL`: webhook URL chinh.
- `DISCORD_WEBHOOK`: bien du phong, van duoc `src/notifier.py` chap nhan.

## Phu thuoc

- `requests`
- `python-dotenv`
- `pytz`

## Ghi chu encoding

Repository nen duoc luu bang UTF-8. Neu terminal hien thi ky tu bi loi, kiem tra lai:

- editor dang luu file voi `UTF-8`
- PowerShell/code page cua may dang doc dung encoding

`.editorconfig` da duoc them de giam loi encoding trong cac lan sua sau.
