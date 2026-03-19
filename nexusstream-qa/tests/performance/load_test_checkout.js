import http from 'k6/http';
import { check, sleep } from 'k6';

/*
 * Simulate high traffic on the Checkout API.
 * Goal: Verify P95 response time is < 500ms under load.
 */
export const options = {
  stages: [
    { duration: '10s', target: 10 },  // Ramp up to 10 users
    { duration: '30s', target: 50 },  // Spike to 50 concurrent users
    { duration: '10s', target: 0 },   // Ramp down
  ],
  thresholds: {
    // Assert that 95% of requests must finish within 500ms
    http_req_duration: ['p(95)<500'], 
    // Assert that less than 1% of requests fail
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  // Simulating a checkout POST request
  const url = 'https://jsonplaceholder.typicode.com/posts';
  const payload = JSON.stringify({
    title: 'Checkout Order #1001',
    body: 'items: [sku-123, sku-456], total: 99.99',
    userId: 1,
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);

  check(res, {
    'status is 201': (r) => r.status === 201,
  });

  sleep(1);
}