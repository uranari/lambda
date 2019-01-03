package main

import (
	"encoding/json"
	"fmt"
	"log"
	"time"

	"github.com/aws/aws-lambda-go/lambda"
)

// CloudWatchEvent から渡されるデータの構造体
type CloudWatchEvent struct {
	Version    string          `json:"version"`
	ID         string          `json:"id"`
	DetailType string          `json:"detail-type"`
	Source     string          `json:"source"`
	AccountID  string          `json:"account"`
	Time       time.Time       `json:"time"`
	Region     string          `json:"region"`
	Resources  []string        `json:"resources"`
	Detail     json.RawMessage `json:"detail"`
}

// CweToLogs は Print で CloudWatch Logs へログを書き込む
func CweToLogs(event CloudWatchEvent) (CloudWatchEvent, error) {
	output, err := json.Marshal(event)
	if err != nil {
		log.Print(err)
		return event, err
	}
	fmt.Print(string(output))
	return event, nil
}

func main() {
	lambda.Start(CweToLogs)
}
