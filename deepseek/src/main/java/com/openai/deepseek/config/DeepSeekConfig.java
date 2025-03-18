package com.openai.deepseek.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.http.HttpHeaders;

@Configuration
public class DeepSeekConfig {
    @Value("${deepseek.api.key}")
    private String apiKey;

    public WebClient getWebClient() {
        return WebClient.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .build();
    }
}