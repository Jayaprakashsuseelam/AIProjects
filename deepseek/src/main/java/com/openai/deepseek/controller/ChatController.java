package com.openai.deepseek.controller;

import com.openai.deepseek.service.AIChatService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;
import java.util.Map;

@RestController
@RequestMapping("/api/chat")
@RequiredArgsConstructor
public class ChatController {
    private final AIChatService aiChatService;

    @PostMapping
    public Mono<ResponseEntity<String>> chat(@RequestBody Map<String, String> request) {
        return aiChatService.getChatResponse(request.get("message"))
                .map(ResponseEntity::ok);
    }
}