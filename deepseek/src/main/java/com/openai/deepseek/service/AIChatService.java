package com.openai.deepseek.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class AIChatService {
    private final WebClient webClient;

    public Mono<String> getChatResponse(String message) {
        return webClient.post()
                .uri("/chat/completions")
                .bodyValue(Map.of("prompt", message))
                .retrieve()
                .bodyToMono(String.class);
    }
}