
# How to create a android version of a activity

## Installing the tools

### Install Cordova

The instructions are [here](http://cordova.apache.org/docs/en/4.0.0//guide_cli_index.md.html#The%20Command-Line%20Interface), in Linux, we do:

```
$ sudo npm install -g cordova
```

### Install dependencies

```
sudo dnf -y install java-1.8.0-openjdk-devel ant android-tools
```

Now, you need to install the Androd SDK from [here](http://developer.android.com/sdk/installing/index.html?pkg=adt)

There is a version with a complete Eclipse IDE and the other "stand-alone",
I have not tried the stand-alone version.

Download the file and unzip, I installed it in the directory:

/home/gonzalo/Android/adt-bundle-linux-x86_64-20140702 

And set the following variables in the env:

```
export ANDROID_HOME=/home/gonzalo/Android/adt-bundle-linux-x86_64-20140702/sdk
export PATH=${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

You need to install the api 19 sdk to build cordova apps. This can be done from Eclipse "SDK Manager"
or from the command line using

```
$ android sdk
```

A window will be opened, and you can select the different SDK versions to downlod.

## Creating the app based in your web activity

```
cordova create find-words-cordova org.sugarlabs.FindWords FindWords
```

This will create a directory find-words-cordova with a skeleton

Move or remove the directory "www"

```
mv www www.old
```

Clone the repository with the web activity in the www directory

```
git clone https://github.com/godiard/find-words-activity.git www
```

Now add the andorid platform

```
cordova platforms add android
```

Edit your config.xml file.
Example:

```
<?xml version='1.0' encoding='utf-8'?>
<widget id="org.sugarlabs.FindWords" version="0.0.1"
    xmlns="http://www.w3.org/ns/widgets"
    xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>FindWords</name>
    <description>
        A game to find hidden words in a grid
    </description>
    <author email="godiard@gmail.com" href="http://cordova.io">
        Gonzalo Odiard
    </author>
    <content src="index.html" />
    <access origin="*" />
    <icon src="res/icon.png" />

    <preference name="DisallowOverscroll" value="true"/>
    <preference name="permissions" value="none"/>
    <preference name="fullscreen" value="true"/>
    <preference name="uiwebviewbounce" value="false"/>
    <preference name="webviewbounce" value="false"/>
    <preference name="disallowoverscroll" value="true"/>
    <preference name="android-minSdkVersion" value="14"/>
</widget>
```

Create a direcory "res" and copy the app icon (in png format) there.

Build the apk

```
cordova build android
```

## Testing the apk

With the "adb" tool is possible install the apk remotely and see the logs

In this case, the ip of my android device is 192.168.0.4

```
$ adb connect 192.168.0.4

$ adb install -r /home/gonzalo/sugar-devel/activities/wordfind/find-words-cordova/platforms/android/ant-build/CordovaApp-debug.apk

```

To see the logs

```
$ adb logcat
```
