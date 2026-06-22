document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // --- Interactive Canvas Background (Node Network) ---
    const canvas = document.getElementById('net-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = (canvas.width = window.innerWidth);
        let height = (canvas.height = window.innerHeight);

        const particles = [];
        const maxParticles = window.innerWidth < 768 ? 40 : 80;
        const connectionDistance = 120;
        const mouse = { x: null, y: null, radius: 150 };

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.8;
                this.vy = (Math.random() - 0.5) * 0.8;
                this.radius = Math.random() * 2 + 1;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;

                // Mouse interaction
                if (mouse.x !== null && mouse.y !== null) {
                    const dx = this.x - mouse.x;
                    const dy = this.y - mouse.y;
                    const dist = Math.hypot(dx, dy);
                    if (dist < mouse.radius) {
                        const force = (mouse.radius - dist) / mouse.radius;
                        this.x += (dx / dist) * force * 2;
                        this.y += (dy / dist) * force * 2;
                    }
                }
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(223, 177, 91, 0.45)';
                ctx.fill();
            }
        }

        // Initialize particles
        for (let i = 0; i < maxParticles; i++) {
            particles.push(new Particle());
        }

        window.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        window.addEventListener('mouseout', () => {
            mouse.x = null;
            mouse.y = null;
        });

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        function animateCanvas() {
            ctx.clearRect(0, 0, width, height);

            // Draw connections
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();

                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.hypot(dx, dy);

                    if (dist < connectionDistance) {
                        const alpha = (1 - dist / connectionDistance) * 0.15;
                        ctx.strokeStyle = `rgba(59, 130, 246, ${alpha})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }

                // Connect to mouse
                if (mouse.x !== null && mouse.y !== null) {
                    const dx = particles[i].x - mouse.x;
                    const dy = particles[i].y - mouse.y;
                    const dist = Math.hypot(dx, dy);
                    if (dist < mouse.radius) {
                        const alpha = (1 - dist / mouse.radius) * 0.25;
                        ctx.strokeStyle = `rgba(223, 177, 91, ${alpha})`;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(mouse.x, mouse.y);
                        ctx.stroke();
                    }
                }
            }

            requestAnimationFrame(animateCanvas);
        }

        animateCanvas();
    }

    // --- Custom Cursor ---
    const cursorDot = document.querySelector('[data-cursor-dot]');
    const cursorOutline = document.querySelector('[data-cursor-outline]');

    if (cursorDot && cursorOutline) {
        window.addEventListener('mousemove', (e) => {
            const posX = e.clientX;
            const posY = e.clientY;

            cursorDot.style.left = `${posX}px`;
            cursorDot.style.top = `${posY}px`;

            cursorOutline.animate({
                left: `${posX}px`,
                top: `${posY}px`
            }, { duration: 400, fill: "forwards" });
        });
    }

    // --- Typewriter Effect for Roles ---
    const typewriterEl = document.querySelector('.role-typewriter');
    if (typewriterEl) {
        const rolesAttr = typewriterEl.getAttribute('data-roles');
        const roles = rolesAttr ? rolesAttr.split(', ') : ['Systems Architect'];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let delay = 100;

        function type() {
            const currentRole = roles[roleIndex];
            if (isDeleting) {
                typewriterEl.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
                delay = 40;
            } else {
                typewriterEl.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
                delay = 90;
            }

            if (!isDeleting && charIndex === currentRole.length) {
                // Pause at the end of the full word
                delay = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                delay = 500;
            }

            setTimeout(type, delay);
        }
        type();
    }

    // --- Interactive Terminal Widget ---
    const terminalInput = document.querySelector('.terminal-input');
    const logsContainer = document.querySelector('.logs-container');
    const termBody = document.querySelector('.terminal-body');

    if (terminalInput && logsContainer) {
        terminalInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const command = terminalInput.value.trim().toLowerCase();
                terminalInput.value = '';

                // Create a row showing the typed command
                const cmdRow = document.createElement('div');
                cmdRow.className = 'log-row';
                cmdRow.innerHTML = `<span style="color: var(--primary-color);">atf$</span> ${command}`;
                logsContainer.appendChild(cmdRow);

                // Run terminal logic
                const outputRow = document.createElement('div');
                outputRow.className = 'log-row';
                outputRow.style.color = '#cbd5e1';
                outputRow.style.borderLeft = '2px solid var(--primary-color)';
                outputRow.style.paddingLeft = '8px';
                outputRow.style.margin = '4px 0 8px 0';

                let reply = '';
                switch (command) {
                    case 'help':
                        reply = 'Available commands:<br>- <b>skills</b>: Dump core developer skills Matrix<br>- <b>about</b>: Print developer background summary<br>- <b>logs</b>: Fetch current system background logs<br>- <b>clear</b>: Clear terminal log output<br>- <b>contact</b>: Display gateway endpoints';
                        break;
                    case 'skills':
                        reply = 'Dumping skills...<br>• Backend: Django, Python, SQL databases<br>• Infrastructure: Celery, Docker, Redis<br>• Logic config: DMN Decision Models<br>• Hardware: FPGA, Computer Hardware, Pynq-z1<br>• Workflow: Agile, Git, SOLID principles';
                        break;
                    case 'about':
                        reply = 'Software Engineer / Systems Architect focused on scalable backend solutions, distributed platforms, parallel execution architectures, and AI KYC integrations. Built on strict SOLID design rules.';
                        break;
                    case 'logs':
                        reply = '[OK] Redis Broker connection active.<br>[OK] Celery workers monitoring task queues.<br>[OK] KYC document originality detector microservice initialized.<br>[INFO] Systems healthy. Load: 0.12.';
                        break;
                    case 'contact':
                        reply = 'Gateway systems configured:<br>- Email: alauddinfaya@gmail.com<br>- Phone/WhatsApp: +967779923330';
                        break;
                    case 'clear':
                        logsContainer.innerHTML = '<div class="log-row" style="color: var(--primary-color);">[Terminal cleared. Type "help" for options.]</div>';
                        termBody.scrollTop = termBody.scrollHeight;
                        return;
                    case '':
                        reply = '';
                        break;
                    default:
                        reply = `Command not recognized: '${command}'. Type 'help' for listing options.`;
                }

                if (reply) {
                    outputRow.innerHTML = reply;
                    logsContainer.appendChild(outputRow);
                }

                // Scroll terminal to bottom
                termBody.scrollTop = termBody.scrollHeight;
            }
        });

        // Add some random log updates every 15-30 seconds to simulate active nodes
        setInterval(() => {
            const mockLogs = [
                'Task scheduler dispatched KYC verification task.',
                'Celery worker node-1 finished process in 24ms.',
                'DMN Rules Evaluated: user access APPROVED.',
                'Heartbeat diagnostic sent: [ALL_SYSTEMS_OK]',
                'Garbage Collector reclaimed 2.4MB memory.'
            ];
            const randomLog = mockLogs[Math.floor(Math.random() * mockLogs.length)];
            const newLog = document.createElement('div');
            newLog.className = 'log-row';
            newLog.style.color = '#64748b';
            newLog.innerHTML = `[${new Date().toLocaleTimeString()}] ${randomLog}`;
            logsContainer.appendChild(newLog);
            termBody.scrollTop = termBody.scrollHeight;
        }, 20000);
    }

    // --- Mobile Menu Toggle ---
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('toggle');
        });

        // Close mobile menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('toggle');
            });
        });
    }

    // --- Sticky Navbar ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
});
