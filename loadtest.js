import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  vus: 100,
  duration: "10m"
};

export default function() {
  let response = http.get("http://myflask-service.com/");
  check(response, {
    "status is 200": (r) => r.status === 200
  });
  sleep(1);
}