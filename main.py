''' Run a function by ado <func_name> '''


from settings import MODE


def set_hook():
    import asyncio
    from settings import HEROKU_APP_NAME, WEBHOOK_URL, BOT_TOKEN
    from aiogram import Bot
    bot = Bot(token=BOT_TOKEN)

    async def hook_set():
        if not HEROKU_APP_NAME:
            print('You have forgot to set HEROKU_APP_NAME')
            quit()
        await bot.set_webhook(WEBHOOK_URL)
        print(await bot.get_webhook_info())
    

    asyncio.run(hook_set())
    bot.close()


def start():
    if MODE == 'webhook':
        print("running mode webhook")
        from bot.webhook import main
        main()
    if MODE == "poller":
        print("running mode poller")
        from aiogram import executor
        from bot.bot import dp
        executor.start_polling(dp, skip_updates=True)
        
if __name__ == "__main__":
    start()