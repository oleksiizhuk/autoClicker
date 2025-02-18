# Lineage 2 Auto Clicker

## Описание
Этот скрипт автоматически нажимает выбранные клавиши в окне выбранного приложения, используя WinAPI SendInput для обхода античит-систем.

## Установка
Перед запуском установите необходимые зависимости.

### **Windows**
1. Установите Python (если не установлен): [Скачать Python](https://www.python.org/downloads/windows/)
2. Установите зависимости:
```bash
pip install pyqt6 pygetwindow keyboard
```
3. Запуск:
```bash
python lineage2_auto_clicker.py
```

### **macOS**
1. Установите Python (если не установлен):
```bash
brew install python
```
2. Создайте и активируйте виртуальное окружение (рекомендуется):
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```bash
pip install pyqt6 pygetwindow pynput
```
4. Запуск:
```bash
python lineage2_auto_clicker.py
```

## Функции
- Выбор окна для отправки нажатий клавиш.
- Выбор клавиши для автоматического нажатия.
- Настройка интервала нажатий.
- **Windows**: Эмуляция клавиатурного ввода через WinAPI SendInput.
- **macOS**: Использование `pynput` для нажатий клавиш.

## Компиляция в .exe (только для Windows)
Если хотите создать исполняемый файл для Windows:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole lineage2_auto_clicker.py
```
После сборки `.exe` файл появится в папке `dist`.

## Советы по безопасности
- Используйте разумные интервалы нажатий, чтобы избежать подозрений.
- Не используйте слишком частые нажатия клавиш (например, каждые 0.01 секунды).
- Программа работает в фоне, убедитесь, что выбрано правильное окно.

