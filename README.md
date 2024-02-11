# replicating-my-linux-desktop-setup

### Pre-requisites

- I am running Fedora 39 on Gnome 45.3 but you should theoretically be able to replicate this on any Linux distribution with Gnome 40 or later.

### Wallpaper 

[Here it is](./1515250514_1.jpg) 

upscale if needed

### My icon theme 

```bash
sudo dnf install papirus-icon-theme
```

Use gnome-tweaks to change the icon theme to 'Papirus-Dark'

```bash
sudo dnf install gnome-tweaks
```
![alt text](/res/image-1.png)

### Fonts I use 

![](/res/myfonts.png)

These fonts are usually included with most Linux distributions. If not, you can install them using the package manager of your distribution.

Other than this, I use the 0xProtoNerdFonts a lot, I've included them [](/fonts/) directory. I am a fan of the MonoLisa font too. It's paid but you can easily find it on the internet. Else, text me, I'll send it to you.

Pro Tip: If any font is unavailable, you can download the ttf file from the internet and place it in the ~/.fonts directory (/home/yourusername/.fonts). Then run the following command to update the font cache.

```bash
fc-cache -f -v
```

### Those Desktop Widgets....

![](/res/desktop.png)

1. Install this extension. We are going to make the widgets using this extension.

https://extensions.gnome.org/extension/5156/desktop-clock/


2. Open the extension settings and click on 'Add Widget'.

![](/res/addwidget.webm)


3. Add a Digital Clock widget and follow these

![](/res/image.png)

Create elements as shown 

![](/res/firstwidget.webm)

Now place [](/scripts/age.py) and [](/scripts/yearprogress.py) in your home directory
Make sure to change the DOB in age.py to your own (line 17)

4. For weather widget create a Custom Widget and follow these

![](/res/weather.webm)

Now place [](/scripts/weather.py) in your home directory. 
Make sure to get API keys from openweathermap and apiip.net and put them in line 104 and 108 of weather.py.

### Extensions

1. Vitals : gives you a system monitor in the top bar.

https://extensions.gnome.org/extension/1460/vitals/

You can customize the appearance of the system monitor by clicking on the settings icon within the extension.

![](/res/Screencast%20from%202024-02-11%2023-52-45.webm)

2. Net Speed Simplified : gives you a network speed monitor in the top bar.

![](/res/netspeed.png)

https://extensions.gnome.org/extension/3724/net-speed-simplified/

You can customize it too. 

![](/res/netspeedconfig.webm)

3. Clipboard History : gives you a clipboard history manager.

![](/res/netspeed.png) 

https://extensions.gnome.org/extension/4839/clipboard-history/

You can configure the number of items to keep in the clipboard history.

4. Systemd Manager : does exactly what the name suggests.

![](/res/systemd.png)

https://extensions.gnome.org/extension/4174/systemd-manager/

5. GSConnect : integrates your Android phone with your desktop in a sorcery-like manner.

You can control your computer from your phone, send and recieve files, deploy a one tap ftp server, and even run commands within the local wi-fi network. No more wires. 

https://extensions.gnome.org/extension/1319/gsconnect/


6. Dash to Dock : gives you a dock, a pretty one 

![](/res/dock.png)

https://extensions.gnome.org/extension/307/dash-to-dock/

You can configure it as much as you want. Here is my configuration.

![](/res/dock.webm)

7. There are more I use but the above are the most important ones. Here is the whole list 

![](/res/extensions.webm)



