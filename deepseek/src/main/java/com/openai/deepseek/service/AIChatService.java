package com.openai.deepseek.service;

import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Service
public class AIChatService {
    private final WebClient webClient;

    public AIChatService(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.baseUrl("https://api.deepseek.com").build();
    }

    public Mono<String> getAIResponse(String prompt) {
        return webClient.post()
                .uri("/v1/generate") // Assuming the endpoint
                .bodyValue("{\"prompt\": \"" + prompt + "\", \"max_tokens\": 100}")
                .retrieve()
                .bodyToMono(String.class);
    }
}