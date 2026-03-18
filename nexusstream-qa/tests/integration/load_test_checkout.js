import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 20 }, // Ramp up to 20 users
    { duration: '1m', target: 20 },  // Stay at 20 users
    { duration: '10s', target: 0 },  // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<200'], // 95% of requests must be faster than 200ms
  },
};

export default function () {
  // Simulate hitting the API endpoint for order creation
  let res = http.post('https://jsonplaceholder.typicode.com/posts', JSON.stringify({
    title: 'Order 123',
    body: 'Load Test Checkout',
    userId: 1,
  }), { headers: { 'Content-Type': 'application/json' } });

  check(res, {
    'status is 201': (r) => r.status === 201,
  });

  sleep(1);
}