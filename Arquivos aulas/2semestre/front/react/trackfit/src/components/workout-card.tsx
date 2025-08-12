interface WorkoutcardProps {

    id: string;
    title: string;
    durationMinutes: number;
    date: string;
    intesity: 1 | 2 | 3 | 4 | 5;

}


export function Workoutcard(props: WorkoutcardProps){
    return (

        <div style={{
            border: "1px solid #ccc",
            padding: "1rem"
        }}>

            <h2>
                {props.title}
            </h2>

            <p>Duração: {props.durationMinutes}</p>

            <p>Itensidade: {props.intesity}</p>

            <p>Data: {props.date}</p>

        </div>
    )
}