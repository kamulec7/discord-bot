import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)



papier = [
    "gazety", "czasopisma", "magazyny", "ulotki", "tektura", "karton", "papier", "książki", "zeszyty", "notesy", "koperty", "opakowania po produktach spożywczych", "opakowania po kosmetykach", "opakowania po chemii gospodarczej"
]
plastik = [
    "folie", "butelki", "plastikowe opakowania", "worki", "opakowania po mleku", "opakowania po jogurtach", "kubki plastikowe", "pojemniki plastikowe", "papierki po cukierkach"
]
bio = [
    "resztki po jedzeniu", "ogryzki", "owoce", "warzywa", "rośliny", "kwiaty", "trawa", "liście", "fusy", "skorupki jajek", "skorupki orzechów"
]
szklo = [
    "szklane butelki", "słoiki", "znicze", "szklane opakowania", "szklane naczynia", "znicz"
]
elektronika = [
    "baterie", "telefony", "głośniki", "słuchawki", "laptop", "żarówki", "telewizory", "komputery", "drukarki", "monitory", "kable", "ładowarki"
]

dobre_nawyki = [
    "Staraj się sortować śmieci",
    "Gasz światło, gdy wychodzisz z pokoju",
    "Zakręcaj wodę podczas mycia zębów",
    "Używaj wielorazowych torb na zakupy",
    "Wydłużaj życie rzeczy – naprawiaj, zamiast od razu wyrzucać",
    "Ograniczaj używanie plastikowych słomek i naczyń jednorazowych",
    "Wietrz mieszkanie krótko, ale intensywnie, zamiast zostawiać uchylone okno"
]

ciekawostki = [
    "Recykling jednej szklanej butelki oszczędza tyle energii, ile potrzeba do świecenia 100-watowej żarówki przez 4 godziny!",
    "Plastikowa butelka potrzebuje nawet 450 lat, aby rozłożyć się w środowisku.",
    "Jedna tonka makulatury pozwala zaoszczędzić około 17 drzew!",
    "Aluminium można przetwarzać w nieskończoność bez utraty jakości."
]

@bot.event
async def on_ready():
    print(f"zalogowano jako {bot.user}")




@bot.command()
async def which_bin(ctx, *, tekst: str):
    if tekst in papier:
        await ctx.send("Wyrzuc to do papieru !")
    elif tekst in plastik:
        await ctx.send("Wyrzuc to do plastiku !")
    elif tekst in bio:
        await ctx.send("Wyrzuc to do kosza bio !")
    elif tekst in szklo:
        await ctx.send("Wyrzuc to do szkla !")
    elif tekst in elektronika:
        await ctx.send("Wyrzuc na pszok albo do specjalnego pojemnika w galerii !")
    else:
        await ctx.send("Nie mamy tego w bazie danych...")


@bot.command()
async def tip(ctx, *, tekst=None):
    await ctx.send(random.choice(dobre_nawyki))

@bot.command()
async def fact(ctx):
    await ctx.send(f"💡 **Czy wiedziałeś, że...** {random.choice(ciekawostki)}")

@bot.command()
async def who(ctx):
    await ctx.send(
        "Siemka! 🌿 Jestem **eko_bot** – Twoim ekologicznym asystentem na Discordzie.\n"
        "Oto moje główne funkcje i komendy, z których możesz korzystać:\n\n"
        "• `!which_bin [przedmiot]` – sprawdzasz w bazie, do którego kosza wyrzucić dany odpad (np. `!which_bin karton`).\n"
        "• `!tip` – losuję dla Ciebie przydatną eko-poradę, jak dbać o środowisko.\n"
        "• `!fact` – podaję ciekawostkę naukową lub ekologiczną.\n"
        "• `!who` – wyświetlam tę wiadomość z listą funkcji!"
    )


bot.run("TWÓJ_TOKEN_BOTA")
