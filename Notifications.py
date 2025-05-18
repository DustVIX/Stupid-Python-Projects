from winotify import Notification, audio

toast = Notification(
    app_id="com.myscript.test", 
    title="تم تهكيرك يا وحش",
    msg="اشوفك بعدين يالهطف هههههههههههه",
    # icon=r"c:\Users\DustVIX\Downloads\windows.png" 
)

toast.set_audio(audio.Default, loop=False)
toast.show()