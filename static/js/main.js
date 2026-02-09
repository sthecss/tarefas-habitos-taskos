const SOUND_MAP = {
    'btn-delete': 'delete.mp3',
    'btn-action': 'snd-add.mp3',
    'btn-check': 'snd-tarefaOk.mp3',
    'btn-restore': 'snd-swap.mp3'
};

const DEFAULT_SOUND = 'snd-all.mp3';

function playSound(file) {
    const audio = new Audio(`/static/audio/${file}`);
    audio.volume = 0.6;
    return audio.play().catch(err => console.warn("Erro ao tocar:", file));
}

document.addEventListener('click', (e) => {
    // Apenas ignora se for o clique NOS TRÊS PONTINHOS (para não tocar som duplo ou bugar)
    if (e.target.innerText === '⋮') return;

    const btn = e.target.closest('button, a, [data-action]');
    if (!btn) return;

    // 1. Resolve o som (data-sound tem prioridade para o caderninho não soar como lixeira)
    let soundFile = btn.dataset.sound;
    if (!soundFile) {
        for (const cls of btn.classList) {
            if (SOUND_MAP[cls]) {
                soundFile = SOUND_MAP[cls];
                break;
            }
        }
    }
    if (!soundFile) soundFile = DEFAULT_SOUND;

    const form = btn.closest('form');

    // 2. Lógica para Formulários (Submit)
    if (form && (btn.type === 'submit' || btn.tagName === 'BUTTON')) {

        // Validação: não envia se estiver vazio (evita erro 422)
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        e.preventDefault();

        // Salva nível para o Level Up
        const lvlElement = document.getElementById('current-level');
        if (lvlElement) {
            localStorage.setItem('pre_click_lvl', lvlElement.innerText.replace('LVL ', ''));
        }

        playSound(soundFile);

        // A pausa de 650ms que você queria para não ficar feio
        setTimeout(() => {
            form.submit();
        }, 650);

    } else {
        // 3. Botões comuns (sem submit)
        playSound(soundFile);
    }
});

// Lógica de Level Up ao carregar
window.addEventListener('load', () => {
    const lvlElement = document.getElementById('current-level');
    const preLvl = localStorage.getItem('pre_click_lvl');

    if (lvlElement && preLvl) {
        const currentLvl = parseInt(lvlElement.innerText.replace('LVL ', ''));
        const oldLvl = parseInt(preLvl);

        if (currentLvl > oldLvl) {
            // Toca o level up com um pequeno delay após o load para garantir o áudio
            setTimeout(() => {
                playSound('snd-levelUp.mp3');
            }, 300);
        }
        localStorage.removeItem('pre_click_lvl');
    }
});
