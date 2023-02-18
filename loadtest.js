import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  vus: 20,
  duration: "10m"
};

export default function() {
  let response = http.get("http://myflask-service.com/compute");
  check(response, {
    "status is 200": (r) => r.status === 200
  });
  sleep(1);
}