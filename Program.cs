using System;
using System.Windows.Forms;

class Program
{
    static void Main()
    {
        NotifyIcon notifyIcon = new NotifyIcon();
        notifyIcon.Icon = new System.Drawing.Icon("img/can-opener.ico");
        notifyIcon.Visible = true;

        ContextMenu contextMenu = new ContextMenu();
        contextMenu.MenuItems.Add("Open Settings", (s, e) => {
            // Open settings dialog
            Console.WriteLine("Settings dialog opened");
        });

        notifyIcon.ContextMenu = contextMenu;

        Application.Run();
    }
}
