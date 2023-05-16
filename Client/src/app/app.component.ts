import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private http:HttpClient){

    const headers= new HttpHeaders()
  .set('ngrok-skip-browser-warning', 'ciao')
    
    this.http.get("https://b854-5-172-64-20.ngrok-free.app", {'headers': headers}).subscribe(
      res => {
        console.log(res)
      },
      err => {
        console.log(err);
      }
    );

    /*fetch("https://838f-5-172-64-20.ngrok-free.app", { credentials: 'include' })
    .then(data => console.log(data))
    .then(ris => console.log(ris))*/
  }

}