from django.shortcuts import render, redirect
from .models import TelegramUser
from aiogram import Bot
import asyncio
import os
from dotenv import load_dotenv
from threading import Thread

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def send_message_to_all(text, user_ids):
    bot = Bot(token=BOT_TOKEN)

    for user_id in user_ids:
        try:
            await bot.send_message(user_id, text)
        except Exception as e:
            print(f"❌ {user_id}: {e}")

    await bot.session.close()


def background_broadcast(text):
    user_ids = list(TelegramUser.objects.values_list("user_id", flat=True))

    async def runner():
        await send_message_to_all(text, user_ids)

    asyncio.run(runner())


def user_list(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            # Запускаем отправку сообщений в отдельном потоке
            Thread(target=background_broadcast, args=(text,)).start()
        return redirect('/')

    users = TelegramUser.objects.all()
    return render(request, 'dashboard/users.html', {'users': users})
