# rpi-audio-guestbook
Audio Guestbook based on raspberry pi + usb audio device (ex: UGREEN)

# Audio test file
Download [piano2.wav](https://www.kozco.com/tech/piano2.wav)

```console
$ wget https://www.kozco.com/tech/piano2.wav
or
$ curl -k https://www.kozco.com/tech/piano2.wav -o piano.wav
```

# Alsa config
Install alsa packages
```console
sudo apt-get install alsa-utils
```

List audio devices
```console
aplay -l
```

Set card in config file. Replace card 0 to card <card number> (cf. audio device list) in file /usr/share/alsa/alsa.conf
```console
defaults.ctl.card 1
defaults.pcm.card 1
```
  
Configure audio level
```console
alsamixer
```
