#!/bin/bash

curl --request POST \
  --url http://localhost:5000/ \
  --header 'Content-Type: application/json' \
  --data '{"data":{"payer":{"dateOfBirth":"1990-01-01T00:00:00+01:00","email":"eddy@helloasso.org","address":"1 rue un","city":"Bordeaux","zipCode":"33000","country":"FRA","firstName":"Eddy","lastName":"MONTUS"},"items":[{"payments":[{"id":7269832,"shareAmount":1000}],"user":{"firstName":"Eddy","lastName":"MONTUS"},"priceCategory":"Free","isCanceled":false,"id":1,"amount":1000,"type":"Payment","initialAmount":0,"state":"Processed"}],"payments":[{"items":[{"id":1,"shareAmount":1000,"shareItemAmount":1000}],"cashOutState":"Transfered","paymentReceiptUrl":"https:\/\/www.helloasso.com\/associations\/demo-boutique\/paiements\/vente-de-noel\/paiement-attestation\/1","id":7269832,"amount":1000,"date":"2021-02-17T09:19:51.2217994+00:00","paymentMeans":"Card","state":"Authorized"}],"amount":{"total":1000,"vat":0,"discount":0},"id":1,"date":"2021-02-17T09:19:40.770879+00:00","formSlug":"vente-de-noel","formType":"PaymentForm","organizationSlug":"demo-boutique"},"eventType":"Order"}'
