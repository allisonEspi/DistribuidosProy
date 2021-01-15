import { Component, OnInit } from "@angular/core";
import {
  Plugins,
  PushNotification,
  PushNotificationToken,
  PushNotificationActionPerformed,
} from "@capacitor/core";

const { PushNotifications } = Plugins;

@Component({
  selector: "app-push-notification",
  templateUrl: "./push-notification.page.html",
  styleUrls: ["./push-notification.page.scss"],
})
export class PushNotificationPage implements OnInit {
  constructor() {}

  ngOnInit() {
    console.log("Initializing Push Notifications");

    PushNotifications.requestPermission().then((result) => {
      if (result.granted) {
        PushNotifications.register();
      } else {
        //Show some error
      }
    });

    PushNotifications.addListener(
      "registration",
      (token: PushNotificationToken) => {
        alert("Push registration sucess, token: " + token.value);
      }
    );

    PushNotifications.addListener("registrationError", (error: any) => {
      alert("Error on registration: " + JSON.stringify(error));
    });

    PushNotifications.addListener(
      "pushNotificationReceived",
      (notification: PushNotification) => {
        alert("Push received: " + JSON.stringify(notification));
      }
    );

    PushNotifications.addListener(
      "pushNotificationActionPerformed",
      (notification: PushNotificationActionPerformed) => {
        alert("Push action performed: " + JSON.stringify(notification));
      }
    );
  }
}
