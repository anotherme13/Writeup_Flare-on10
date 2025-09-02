Oke, this is an android challenge. At first glance, I just thought that we have to hack or do something illegal with the in-game assets. However, closer inspection reveals different: the firebase is implemented to leverage from a notification channel to a C2 channel so that whenever user start the app, it will communication with the firebase, transfer player machine's information, etc...
All suspicious things is located at function **f** when we disassmple the app using jadx. Actually, when I implemented, I tried 2 possible cases that the input file is **iv.png** or **ps.png**. And these are the results:
![ps.png](./decrypted_ps.png)
![iv.png](./decrypted_iv.png)
