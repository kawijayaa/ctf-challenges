type Props = {
    message: string,
    sender?: string,
    sent?: boolean
}

export default function ChatBubble(props: Props) {
    return (
        <div className={`rounded-xl p-4 flex flex-col w-content ${props.sent ? 'self-end bg-blue-900' : 'self-start bg-neutral-700'}`}>
            <div className="font-bold">{props.sender}</div>
            <div>{props.message}</div>
        </div>
    );
}
