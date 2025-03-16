package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"encoding/json"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"
	"github.com/gorilla/websocket"
)

type Message struct {
	Message string `json:"message"`
	Sender  string `json:"sender"`
}

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
	CheckOrigin:     func(r *http.Request) bool { return true },
}

func generateToken(sub string) (string, error) {
	claims := jwt.MapClaims{
		"sub": sub,
		"exp": time.Now().Add(time.Minute * 5).Unix(),
		"iat": time.Now().Unix(),
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString([]byte(os.Getenv("JWT_SECRET")))
}

func closeConnection(conn *websocket.Conn) {
	log.Println("Closing connection")
	conn.Close()
}

func handleWebsocket(conn *websocket.Conn, sub string) {
	defer closeConnection(conn)
	for {
		_, messageJson, err := conn.ReadMessage()
		if err != nil {
			log.Println(err)
			break
		}

		var message Message
		json.Unmarshal(messageJson, &message)

		if message.Message == "/flag" {
			if message.Sender == sub && message.Sender == "staff" {
				message := Message{
					Message: os.Getenv("FLAG"),
					Sender:  "WeebSocks Staff",
				}
				messageJson, err := json.Marshal(message)
				if err != nil {
					log.Println(err)
					break
				}
				conn.WriteMessage(websocket.TextMessage, messageJson)
			} else {
				message := Message{
					Message: "only i can get the flag :>",
					Sender:  "WeebSocks Staff",
				}
				messageJson, err := json.Marshal(message)
				if err != nil {
					log.Println(err)
					break
				}
				conn.WriteMessage(websocket.TextMessage, messageJson)
			}
		} else if message.Message == "/generate" && message.Sender != "user" {
			tokenString, err := generateToken(message.Sender)
			if err != nil {
				log.Println(err)
				break
			}
			message := Message{
				Message: tokenString,
				Sender:  "WeebSocks Staff",
			}
			messageJson, err := json.Marshal(message)
			if err != nil {
				log.Println(err)
				break
			}
			conn.WriteMessage(websocket.TextMessage, messageJson)
		} else {
			message := Message{
				Message: "idk what u talkin bout",
				Sender:  "WeebSocks Staff",
			}
			messageJson, err := json.Marshal(message)
			if err != nil {
				log.Println(err)
				break
			}
			conn.WriteMessage(websocket.TextMessage, messageJson)
		}
	}
}

func main() {
	router := gin.Default()
	router.Use(cors.New(cors.Config{
		AllowAllOrigins: true,
		AllowMethods:    []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowHeaders:    []string{"Origin", "Content-Length", "Content-Type"},
		ExposeHeaders:   []string{"Content-Length"},
		MaxAge:          300,
	}))
	router.GET("/api/token/generate", func(c *gin.Context) {
		tokenString, err := generateToken("user")
		if err != nil {
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}
		c.JSON(200, gin.H{"data": tokenString})
	})
	router.GET("/api/ws", func(c *gin.Context) {
		token, ok := c.GetQuery("token")
		if !ok {
			c.JSON(401, gin.H{"error": "token not found"})
			return
		}

		claims, err := jwt.Parse(token, func(token *jwt.Token) (interface{}, error) {
			return []byte(os.Getenv("JWT_SECRET")), nil
		})
		if err != nil {
			log.Println(err)
			c.JSON(401, gin.H{"error": "invalid token"})
			return
		}

		if !claims.Valid {
			log.Println(err)
			c.JSON(401, gin.H{"error": "invalid token"})
			return
		}

		conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
		if err != nil {
			log.Println(err)
			c.JSON(400, gin.H{"error": err.Error()})
			return
		}
		go handleWebsocket(conn, claims.Claims.(jwt.MapClaims)["sub"].(string))
	})
	router.Run(":8080")
}
