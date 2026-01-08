
interface LogButtonProps {
    severity: 'info' | 'warning' | 'error';
    title: string;
    username?: string;
}

function formatSeverity(severity: string): string {
    switch (severity) {
        case 'info':
            return '[INFO]';
        case 'warning':
            return '[WARNING]';
        case 'error':
            return '[ERROR]';
        default:
            return '[UNKNOWN]';
    }
}

export default function LogButton({ severity, title, username }: LogButtonProps) {
    // TODO: This will instead send a message to Kafka
    const handleClick = () => {
        console.log(`${formatSeverity(severity)} message clicked by ${username}`);
    };

    return (
        <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 hover:cursor-pointer" onClick={handleClick}>
            {title}
        </button>
    );
}