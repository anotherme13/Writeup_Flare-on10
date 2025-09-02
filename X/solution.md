So basically, I just opened X.dll with Dnspy and after examining each method carefully, I found out the flag inside the _lockButton_Click method.
```C#
// monogame1.Game1
// Token: 0x06000023 RID: 35 RVA: 0x000027F0 File Offset: 0x000009F0
private async void _lockButton_Click(object sender, EventArgs e)
{
	if (this._digitDisplays[0].Value * 10 + this._digitDisplays[1].Value == 42)
	{
		this._backgroundDisplay.State = BackgroundDisplay.BackgroundStates.Success;
		await MessageBox.Show("Welcome to Flare-On 10", "Congratulations!\n glorified_captcha@flare-on.com", new string[] { "Ok" });
	}
	else
	{
		this._backgroundDisplay.State = BackgroundDisplay.BackgroundStates.Failure;
	}
}

```
-> flag: **glorified_captcha@flare-on.com**
