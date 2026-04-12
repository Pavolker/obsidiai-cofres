// Configuração (mudar API_BASE para a URL do Railway quando fizer deploy)
const API_BASE = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" 
    ? "http://localhost:8000/api" 
    : "https://SEU-APP-RAILWAY.up.railway.app/api";

// Elementos da UI
const menuItems = document.querySelectorAll('.menu-item');
const views = document.querySelectorAll('.view');
const statChunks = document.getElementById('stat-chunks');

const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const resultsContainer = document.getElementById('resultsContainer');

const chatInput = document.getElementById('chatInput');
const sendMessageBtn = document.getElementById('sendMessageBtn');
const chatHistory = document.getElementById('chatHistory');

// Estado do Chat
let chatMessages = [];

// Inicialização
document.addEventListener("DOMContentLoaded", () => {
    fetchStats();
    
    // Navegação do Menu
    menuItems.forEach(item => {
        item.addEventListener('click', (e) => {
            menuItems.forEach(mi => mi.classList.remove('active'));
            e.currentTarget.classList.add('active');
            
            const viewId = e.currentTarget.getAttribute('data-view');
            views.forEach(view => view.classList.remove('active-view'));
            document.getElementById(`view-${viewId}`).classList.add('active-view');
        });
    });

    // Busca
    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performSearch();
    });

    // Chat
    sendMessageBtn.addEventListener('click', sendChatMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendChatMessage();
        }
    });
});

// Funções de API
async function fetchStats() {
    try {
        const res = await fetch(`${API_BASE}/stats`);
        const data = await res.json();
        statChunks.innerText = data.total_chunks || 0;
    } catch (err) {
        console.error("Erro ao buscar stats", err);
        statChunks.innerText = "Offline";
    }
}

async function performSearch() {
    const query = searchInput.value.trim();
    if (!query) return;

    resultsContainer.innerHTML = '<div class="empty-state">Buscando na sua rede...</div>';
    
    try {
        const res = await fetch(`${API_BASE}/search`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query, limit: 10 })
        });
        
        if (!res.ok) throw new Error("Erro na API");
        const data = await res.json();
        
        renderSearchResults(data.results);
    } catch (err) {
        resultsContainer.innerHTML = '<div class="empty-state" style="color: #D97757">Falha ao conectar com o cofre. Verifique se o servidor está rodando.</div>';
    }
}

function renderSearchResults(results) {
    if (!results || results.length === 0) {
        resultsContainer.innerHTML = '<div class="empty-state">Nenhuma nota encontrada com esse significado. Tente outros termos.</div>';
        return;
    }

    resultsContainer.innerHTML = '';
    results.forEach(result => {
        const card = document.createElement('div');
        card.className = 'result-card';
        card.innerHTML = `
            <div class="result-meta">
                <span class="badge-vault">${result.vault}</span>
                <span class="badge-path">${result.filepath}</span>
            </div>
            <p>${result.content.replace(/\n/g, '<br>')}</p>
        `;
        resultsContainer.appendChild(card);
    });
}

// Chat Lógica
async function sendChatMessage() {
    const text = chatInput.value.trim();
    if (!text) return;
    
    chatInput.value = '';
    
    // Adiciona na UI
    appendMessageToChat('user', text);
    
    // Guarda na memoria
    chatMessages.push({ role: "user", content: text });
    
    // Mostra "Digitando..."
    const loadingId = appendLoadingMessage();

    try {
        const res = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ messages: chatMessages })
        });
        
        document.getElementById(loadingId).remove();
        
        if (!res.ok) throw new Error("Erro na resposta da AI");
        const data = await res.json();
        
        chatMessages.push({ role: "assistant", content: data.reply });
        appendMessageToChat('ai', data.reply);
        
    } catch (err) {
        document.getElementById(loadingId).remove();
        appendMessageToChat('ai', "Desculpe, ocorreu um erro ao acessar o seu cofre.");
    }
}

function appendMessageToChat(role, text) {
    const div = document.createElement('div');
    div.className = `message ${role}-message`;
    
    const avatar = role === 'user' ? '👤' : '✨';
    
    // Convert linebreaks to br
    const formattedText = text.replace(/(?:\r\n|\r|\n)/g, '<br>');
    
    div.innerHTML = `
        <div class="avatar">${avatar}</div>
        <div class="bubble">${formattedText}</div>
    `;
    
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function appendLoadingMessage() {
    const id = `msg-${Date.now()}`;
    const div = document.createElement('div');
    div.className = `message ai-message`;
    div.id = id;
    div.innerHTML = `
        <div class="avatar">✨</div>
        <div class="bubble">...</div>
    `;
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
    return id;
}
