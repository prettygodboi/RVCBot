# RVCBot

Бот переозвучивания голосовых сообщений в Telegram.
Проект использует нейронную сеть Retrieval Voice Conversion (RVC)
https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

## Доступные команды
1. /start - меню приветствия бота
2. /voice <голос> - выбор голоса для переозвучивания

После выбора голоса боту достаточно отправить голосовое сообщение - в ответ придет обработанная запись

## Зависимости
- Python 3.9 или новее
- Pyrogram 2.0.100

Для работы требуется запущенная RVC WebUI с поддержкой Gradio API

## Конфигурация
secrets.json - данные для авторизации телеграмм бота (https://core.telegram.org/bots)
voices.json - доступные голоса
gradio.json - хост Gradio для доступа к API

## Авторы
Разработано студентами Уральского Федерального университета (УрФУ)

- [Сергеев Илья](https://github.com/allwanttokissme)
- [Шевляков Дмитрий](https://github.com/prettygodboi)
