# Opening WinHelp Files on Windows 10

[WinHelp](https://en.wikipedia.org/wiki/WinHelp) is an old format for help files that was widely used in the 1990s and early 2000s. Files using this format usually have the extension `hlp`.

In newer versions of Windows, the program required to open help files stored using WinHelp format was replaced by a stub that simply opens [this page on Microsoft's support site](https://support.microsoft.com/en-us/topic/error-opening-help-in-windows-based-programs-feature-not-included-or-help-not-supported-3c841463-d67c-6062-0ee7-1a149da3973b), which states:

> The Windows Help program is not supported in Windows 10, Windows Server 2012 or later versions of Windows Server. The Windows Help program is available for Windows Vista, 7, 8 and 8.1 only.

The page links to updates for Windows 8.1 and earlier versions of Windows that enable them to open WinHelp files, but these aren't helpful for users of Windows 10.

## The Initial Situation on Windows 10

Initially, Windows 10 contains an executable named `winhlp32.exe` in `C:\Windows` (there may be additional copies elsewhere, e.g., in `C:\Windows\WinSxS\wow64[...]`). This is the stub program discussed above. It has an MD5 hash of `0629e6d130f226c009ea9ab329f37acc` (obtained by running `certutil -hashfile winhlp32.exe MD5` in a PowerShell window).

## Adding WinHelp Support to Windows 10

* Download `winhlp32.msi` from [this page on majorgeeks.com](https://www.majorgeeks.com/files/details/winhlp32_for_windows_10.html) (I've also stored a copy [here](winhlp32.msi)).
  * The MD5 hash of this file should be `10ba7330eab7dbaec93bee5112df47d4`. As with any executable, I'd also recommend scanning it with your anti-malware software of choice just to be on the safe side.
  * The original source is [RAX Software](https://raxsoft.com/raxccm/software_app.php?progid=13).
* Run `winhlp32.msi`. Doing so will create a directory at `C:\Windows\WinHelp` containing a functional version of `winhlp32.exe` (MD5 hash: `11c3acf585f167569e76b9bdd9961fa7`) and associate it with WinHelp files.
* At this point, trying to open a WinHelp file should result in the new, functional copy of `winhlp32.exe` being called (rather than the stub included with Windows 10), allowing you to view the file.

If your computer has a high-DPI display, you may notice that help files are blurry. To resolve this:

* Open File Explorer and navigate to the `C:\Windows\WinHelp` directory.
* Right-click on `winhlp32.exe` and select "Properties" from the context menu.
* On the "Compatibility" tab and press the "Change high DPI settings" button.
* In the "High DPI scaling override" section, enable "Override high DPI scaling behavior" and select "Application" from the "Scaling performed by" drop-down menu.
* Save the changes.

## "Decompiling" WinHelp Files

*This isn't a particularly convenient way to view WinHelp files but is included for reference.*

WinHelp files typically consist of a text file in [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format), some metadata, and whatever images were included (usually stored as [indexed-colour](https://en.wikipedia.org/wiki/Indexed_color) bitmaps). These files can be extracted using an old program called HelpDeco (created by a person named Manfred Winterhoff), which as of late 2021 is still available from [an archived copy of the HelpDeco site](https://www.oocities.org/mwinterhoff/helpdeco.htm) on OoCities (an archive of [GeoCities](https://en.wikipedia.org/wiki/Yahoo!_GeoCities) sites). There's some information regarding HelpDeco in [this Stack Overflow answer from 2009](https://superuser.com/a/32485) and [this comment from 2021](https://superuser.com/questions/32452/converting-windows-help-file-to-a-more-user-friendly-format#comment2550461_32485).

I've taken the liberty of storing a copy of `helpdeco.zip` (which contains the HelpDeco program) [here](helpdeco.zip) in case it becomes unavailable in the future. The HelpDeco site and `helpdeco.zip` are also available on the Internet Archive's Wayback Machine [here](https://web.archive.org/web/20210422195708/https://www.oocities.org/mwinterhoff/helpdeco.htm) and [here](https://web.archive.org/web/20210422195708/https://www.oocities.org/mwinterhoff/helpdeco.zip), respectively.
