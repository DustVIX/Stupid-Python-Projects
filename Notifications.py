from winotify import Notification, audio

toast = Notification(
    app_id="Windows Security", 
    title="Windows Security",
    msg="يا عبد",
    icon=r"c:\Users\DustVIX\Downloads\windows.ico" 
)

toast.add_actions(label="موافق", launch="C:\\path\\to\\file.txt")
toast.set_audio(audio.Default, loop=False)
toast.show()