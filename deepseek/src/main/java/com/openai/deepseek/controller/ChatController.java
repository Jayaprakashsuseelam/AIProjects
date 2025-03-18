package com.openai.deepseek.controller;

import com.openai.deepseek.service.AIChatService;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api/chat")
public class ChatController {
    private final AIChatService deepSeekService;

    public ChatController(AIChatService deepSeekService) {
        this.deepSeekService = deepSeekService;
    }

    @GetMapping
    public Mono<String> chat(@RequestParam String message) {
        return deepSeekService.getAIResponse(message);
    }
}