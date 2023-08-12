extern crate systray;

fn main() {
    match systray::Application::new() {
        Ok(mut app) => {
            app.set_icon_from_file(&"img/can-opener.ico").ok();
            app.add_menu_item(&"Open Settings", |_| {
                // Open settings dialog
                println!("Settings dialog opened");
                Ok::<_, systray::Error>(())
            }).ok();
            app.wait_for_message();
        },
        Err(e) => println!("Can't create system tray application: {}", e),
    }
}
